#!/usr/bin/env python3
"""Capability dependency graph validator.

An example, not a rule. Copy it into your own project and change it there; do
not edit it in place, and do not read it as the way this has to be done.
`zoe-sdlc-components` says what must hold — how the system connects together is
one graph, declared in a form a program can read, and checked by one — and
deliberately leaves the format and the tooling to you. This file is
one working answer, written for one particular set of conditions, kept because a
working answer is easier to adapt than a blank page.

The conditions it was written for
---------------------------------
Everything below is an assumption of this implementation, not a rule of the ZOE
SDLC base. Where your project differs, change the script or write your own.

- Declarations live in markdown specification files, one file per component,
  under a single directory tree (`--specs-dir`, `docs/components` by default).
- Each specification declares what it depends on in a fenced YAML block:

      component: CMP.COMPONENT_CODE
      dependencies:
        CAP.CAPABILITY1:
          - CMP.OTHER1:
            - CAP.SOME_CAPABILITY
            - CAP.ANOTHER_CAPABILITY
          - CMP.OTHER2:
            - CAP.YET_ANOTHER_CAPABILITY

  A capability with no dependencies is declared with an empty list. Any other
  fenced YAML block in the file is ignored unless it has a `component` key.
- Identifiers follow a `CMP.` / `CAP.` convention, and a capability's name only
  has to be unique within its component: the script qualifies each one with its
  owning component, so `CAP.STORAGE` declared under `CMP.B` becomes
  `CMP.B.CAP.STORAGE` in the graph.
- A dependency may name a component by an unambiguous suffix of its code rather
  than in full; ambiguous suffixes are reported and left unresolved.
- Components and capabilities outside the project are marked by an `X` segment
  in their code (`X.` at the start, or `.X.` within). They are counted
  separately and are otherwise ordinary nodes.
- Files named `README.md` or `IDEAS.md`, and anything under a `templates` or
  `tasks` directory, are not specifications.
- PyYAML and networkx are available. Neither is required by the base; they are
  what this implementation happens to use.

What it checks
--------------
Loops in the graph; references to capabilities no specification defines; a
capability depending on another capability of its own component, which the base
rules out because a component's internal structure is not a dependency between
components; nodes with nothing pointing at them and nothing they point at; and
fields in a dependency block outside the recognised set.

A dependency on a sub-component is not a dependency on your own component: a
sub-component has its own code, so `CMP.A.SUB` depending on `CMP.A` is an
ordinary dependency and is not reported.

Disconnected nodes are reported but do not fail the run, on the assumption that
a component can legitimately sit unconnected for a while. Everything else fails
it.

Usage:
    python validate_capability_graph.py [--specs-dir DIRECTORY] [--output REPORT_FILE]

Exits 0 when the graph passes and 1 when it does not, so it can run as a test
or a build step and fail the work that depends on it.
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

import yaml

try:
    import networkx as nx
except ImportError:
    print("ERROR: networkx is required. Install with: pip install networkx", file=sys.stderr)
    sys.exit(1)

# Fields recognised inside a dependency block; anything else is reported.
KNOWN_YAML_FIELDS = {'component', 'dependencies'}


def extract_yaml_blocks(markdown_content: str) -> List[str]:
    """
    Extract all YAML code blocks from markdown content.
    Args:
        markdown_content: The markdown file content as a string

    Returns:
        List of YAML block contents (without the fence markers)
    """
    # Pattern to match ```yaml ... ``` blocks
    pattern = r'```yaml\s*\n(.*?)\n```'
    matches = re.findall(pattern, markdown_content, re.DOTALL)
    return matches


def parse_dependencies(yaml_content: str, source_file: Optional[Path] = None) -> Tuple[str, Dict[str, List[Tuple[str, str]]], List[str]]:
    """
    Parse the dependencies section from a YAML block.

    Format:
    component: CMP.COMPONENT_CODE
    dependencies:
      CAP.CAPABILITY1:
        - CMP.OTHER1:
          - CAP.SOME_CAPABILITY
          - CAP.ANOTHER_CAPABILITY
        - CMP.OTHER2:
          - CAP.YET_ANOTHER_CAPABILITY

    Args:
        yaml_content: YAML content as string
        source_file: Optional path to the source file (for diagnostics)

    Returns:
        Tuple of (component_code, dependencies_dict, warnings) where:
        - component_code: The component code from the YAML
        - dependencies_dict: Maps capability codes to list of (component, capability) tuples
        - warnings: List of warning messages (e.g. unknown fields)
    """
    try:
        data = yaml.safe_load(yaml_content)
        if not data or not isinstance(data, dict):
            return "", {}, []

        warnings: List[str] = []

        component_code = data.get('component', '')
        if not component_code:
            location = f" in {source_file}" if source_file else ""
            print(f"WARNING: No 'component' field in YAML block{location}", file=sys.stderr)
            return "", {}, []

        # Validate fields against known set
        unknown_fields = set(data.keys()) - KNOWN_YAML_FIELDS
        for field in sorted(unknown_fields):
            msg = f"Unknown field '{field}' in dependency block of {component_code}"
            warnings.append(msg)
            print(f"WARNING: {msg}", file=sys.stderr)

        if 'dependencies' not in data:
            return component_code, {}, warnings

        deps = data['dependencies']
        if not isinstance(deps, dict):
            print(f"WARNING: 'dependencies' is not a dict in {component_code}, "
                  f"got {type(deps).__name__}", file=sys.stderr)
            return component_code, {}, warnings

        result: Dict[str, List[Tuple[str, str]]] = {}

        for cap, dep_list in deps.items():
            if dep_list is None or dep_list == []:
                result[cap] = []
            elif isinstance(dep_list, list):
                parsed_deps = []
                for item in dep_list:
                    if isinstance(item, dict):
                        # Nested format: {CMP.X: [CAP.Y, CAP.Z]}
                        for component, capabilities in item.items():
                            if capabilities and isinstance(capabilities, list):
                                for capability in capabilities:
                                    parsed_deps.append((component, capability))
                    elif isinstance(item, str):
                        # Flat format: a dependency named without its component
                        print(f"WARNING: Flat dependency format: {item}",
                              file=sys.stderr)
                result[cap] = parsed_deps
            else:
                result[cap] = []
        return component_code, result, warnings
    except yaml.YAMLError as e:
        print(f"WARNING: Failed to parse YAML: {e}", file=sys.stderr)
        return "", {}, []


def extract_component_code(markdown_content: str) -> str:
    """
    Extract the component code from the markdown frontmatter or content.
    Args:
        markdown_content: The markdown file content

    Returns:
        Component code string or empty string if not found
    """
    # Try to find in frontmatter
    frontmatter_match = re.search(r'^code:\s*(\S+)', markdown_content, re.MULTILINE)
    if frontmatter_match:
        return frontmatter_match.group(1)
    # Try to find in body: **Code:** `CMP.X.Y`
    code_match = re.search(r'\*\*Code:\*\*\s*`([^`]+)`', markdown_content)
    if code_match:
        return code_match.group(1)
    return ""


def find_spec_files(specs_dir: Path) -> List[Path]:
    """
    Find all component specification markdown files.
    Args:
        specs_dir: Directory to search for specs

    Returns:
        List of Path objects for spec files
    """
    # Look for markdown files, excluding templates and certain directories
    spec_files = []
    for md_file in specs_dir.rglob('*.md'):
        # Skip templates, tasks, and other non-spec directories
        path_parts = md_file.parts
        if any(skip in path_parts for skip in ['templates', 'tasks', 'IDEAS.md', 'README.md']):
            continue
        spec_files.append(md_file)
    return spec_files


def build_dependency_graph(specs_dir: Path) -> Tuple[nx.DiGraph, Dict[str, Path], Set[str], List[str]]:
    """
    Build a directed graph with two node types:
    - Component nodes (e.g., CMP.A, CMP.B)
    - Capability nodes (e.g., CMP.A.CAP.STORAGE, CMP.B.CAP.VALIDATION)

    Capability names are qualified with their providing component's code to form
    globally unique identifiers: a capability CAP.STORAGE declared under component
    CMP.B is CMP.B.CAP.STORAGE in the graph, so capability names only have to be
    unique within their own component.

    Edges:
    - Component -> Capability: component provides this capability
    - Capability -> Capability: capability depends on another capability

    Args:
        specs_dir: Directory containing component specifications

    Returns:
        Tuple of (graph, file_map, all_capabilities, all_warnings)
        - graph: NetworkX directed graph with node_type attribute
        - file_map: Mapping of qualified capability codes to their source files
        - all_capabilities: Set of all qualified capability codes defined
        - all_warnings: List of warning messages from parsing
    """
    spec_files = find_spec_files(specs_dir)
    print(f"Found {len(spec_files)} specification files")

    # --- First pass: collect all component codes and parsed data ---
    parsed_specs: List[Tuple[Path, str, Dict[str, List[Tuple[str, str]]]]] = []
    all_component_codes: Set[str] = set()
    all_warnings: List[str] = []

    for spec_file in spec_files:
        try:
            content = spec_file.read_text(encoding='utf-8')
            yaml_blocks = extract_yaml_blocks(content)

            for yaml_block in yaml_blocks:
                component_code, deps, warnings = parse_dependencies(yaml_block, spec_file)
                all_warnings.extend(warnings)
                if component_code:
                    all_component_codes.add(component_code)
                    parsed_specs.append((spec_file, component_code, deps))
        except Exception as e:
            print(f"ERROR processing {spec_file}: {e}", file=sys.stderr)
            continue

    # --- Build component code resolution map (suffix -> full code) ---
    # Allows specs to reference components by suffix (e.g. STORE.DB instead of
    # SHOP.APP.STORE.DB) as long as the suffix is unambiguous.
    _code_resolution: Dict[str, str | None] = {}
    for code in all_component_codes:
        parts = code.split('.')
        for i in range(len(parts)):
            suffix = '.'.join(parts[i:])
            if suffix in _code_resolution:
                if _code_resolution[suffix] != code:
                    _code_resolution[suffix] = None  # ambiguous
            else:
                _code_resolution[suffix] = code

    def resolve_component_code(ref: str) -> str:
        """Resolve a potentially short component reference to its full code."""
        if ref in all_component_codes:
            return ref  # already a full code
        resolved = _code_resolution.get(ref)
        if resolved:
            return resolved
        print(f"WARNING: Could not resolve component reference '{ref}'",
              file=sys.stderr)
        return ref  # unresolved — use as-is

    # --- Second pass: build graph with qualified capability names ---
    G: nx.DiGraph = nx.DiGraph()
    file_map: Dict[str, Path] = {}
    all_capabilities: Set[str] = set()

    for spec_file, component_code, deps in parsed_specs:
        # Add component node (add_node merges attrs on existing nodes)
        G.add_node(
            component_code,
            node_type='component',
            source_file=str(spec_file)
        )

        for capability, dep_list in deps.items():
            # Qualify capability with its providing component
            qualified_cap = f"{component_code}.{capability}"

            all_capabilities.add(qualified_cap)
            file_map[qualified_cap] = spec_file

            # add_node merges attrs on existing nodes, so auto-created
            # dependency targets get node_type set when their spec is processed.
            # 'component' records which component owns the capability, so a
            # dependency on one's own component can be told apart from a
            # dependency on another component's capability.
            G.add_node(
                qualified_cap,
                node_type='capability',
                component=component_code,
                source_file=str(spec_file)
            )

            # Component provides this capability
            G.add_edge(component_code, qualified_cap)

            # Add capability dependencies (qualified with dep component)
            for dep_component, dep_capability in dep_list:
                resolved_dep = resolve_component_code(dep_component)
                qualified_dep_cap = f"{resolved_dep}.{dep_capability}"
                G.add_node(qualified_dep_cap, component=resolved_dep)
                G.add_edge(qualified_cap, qualified_dep_cap)

    return G, file_map, all_capabilities, all_warnings


def validate_graph(G: nx.DiGraph, all_capabilities: Set[str], all_warnings: Optional[List[str]] = None) -> dict:
    """
    Validate the dependency graph and collect issues.
    Args:
        G: Directed graph of dependencies
        all_capabilities: Set of all defined capability codes
        all_warnings: Optional list of warnings from parsing (e.g. unknown fields)

    Returns:
        Dictionary containing validation results and issues
    """
    # Separate internal and external nodes
    internal_components = set()
    external_components = set()
    internal_capabilities = set()
    external_capabilities = set()

    for node in G.nodes():
        node_type = G.nodes[node].get('node_type')
        # Assumed convention: external components and capabilities carry an X
        # segment in their code — '.X.' within it, or 'X.' at the start.
        is_external = '.X.' in node or node.startswith('X.')

        if node_type == 'component':
            if is_external:
                external_components.add(node)
            else:
                internal_components.add(node)
        elif node_type == 'capability':
            if is_external:
                external_capabilities.add(node)
            else:
                internal_capabilities.add(node)

    results: Dict[str, Any] = {
        'is_dag': True,
        'cycles': [],
        'disconnected': [],
        'invalid_refs': [],
        'self_dependencies': [],
        'unknown_fields': all_warnings or [],
        'total_capabilities': len(all_capabilities),
        'total_edges': G.number_of_edges(),
        'internal_components': len(internal_components),
        'external_components': len(external_components),
        'internal_capabilities': len(internal_capabilities),
        'external_capabilities': len(external_capabilities),
    }
    # Check the graph has no loops
    try:
        results['is_dag'] = nx.is_directed_acyclic_graph(G)
        if not results['is_dag']:
            # Find cycles
            try:
                cycles = list(nx.simple_cycles(G))
                results['cycles'] = cycles
            except Exception as e:
                results['cycles'] = [f"Error finding cycles: {e}"]
    except Exception as e:
        results['is_dag'] = False
        results['cycles'] = [f"Error checking for loops: {e}"]
    # Find disconnected nodes (no connections at all)
    for node in G.nodes():
        in_degree = G.in_degree(node)
        out_degree = G.out_degree(node)
        if in_degree == 0 and out_degree == 0:
            results['disconnected'].append(node)
    # Find invalid references (capabilities referenced but not defined)
    for node in G.nodes():
        for successor in G.successors(node):
            if successor not in all_capabilities:
                results['invalid_refs'].append({
                    'from': node,
                    'to': successor,
                    'reason': 'Referenced capability not defined'
                })
    # Find capabilities depending on their own component's capabilities.
    # A sub-component has its own code, so only an exact match counts.
    for node in G.nodes():
        if G.nodes[node].get('node_type') != 'capability':
            continue
        owner = G.nodes[node].get('component')
        if not owner:
            continue
        for successor in G.successors(node):
            if G.nodes[successor].get('component') == owner:
                results['self_dependencies'].append({
                    'from': node,
                    'to': successor,
                    'component': owner
                })
    return results


def generate_report(results: dict, output_file: Optional[Path] = None) -> str:
    """
    Generate a human-readable validation report.
    Args:
        results: Validation results dictionary
        output_file: Optional path to write report to

    Returns:
        Report text
    """
    lines = []
    lines.append("=" * 80)
    lines.append("CAPABILITY DEPENDENCY REPORT")
    lines.append("=" * 80)
    lines.append("")
    lines.append(f"Internal Components: {results['internal_components']}")
    lines.append(f"External Components: {results['external_components']}")
    lines.append(f"Internal Capabilities: {results['internal_capabilities']}")
    lines.append(f"External Capabilities: {results['external_capabilities']}")
    lines.append(f"Total Capabilities: {results['total_capabilities']}")
    lines.append(f"Total Dependencies: {results['total_edges']}")
    lines.append(f"Free of loops: {'YES' if results['is_dag'] else 'NO'}")
    lines.append("")
    # Cycles
    if results['cycles']:
        lines.append("LOOPS DETECTED:")
        lines.append("-" * 80)
        for i, cycle in enumerate(results['cycles'], 1):
            if isinstance(cycle, str):
                lines.append(f"  {i}. {cycle}")
            else:
                cycle_str = ' -> '.join(cycle + [cycle[0]])
                lines.append(f"  {i}. {cycle_str}")
        lines.append("")
    else:
        lines.append("OK: no loops detected")
        lines.append("")
    # Disconnected nodes
    if results['disconnected']:
        lines.append("DISCONNECTED NODES:")
        lines.append("-" * 80)
        lines.append("(No dependencies of their own, and nothing depends on them)")
        for node in results['disconnected']:
            lines.append(f"  - {node}")
        lines.append("")
    else:
        lines.append("OK: no disconnected nodes")
        lines.append("")
    # Invalid references
    if results['invalid_refs']:
        lines.append("INVALID REFERENCES:")
        lines.append("-" * 80)
        lines.append("(Capabilities referenced but not defined in any specification)")
        for ref in results['invalid_refs']:
            lines.append(f"  - {ref['from']} -> {ref['to']}")
            lines.append(f"    Reason: {ref['reason']}")
        lines.append("")
    else:
        lines.append("OK: no invalid references")
        lines.append("")
    # Dependencies on one's own component
    if results['self_dependencies']:
        lines.append("DEPENDENCIES WITHIN A COMPONENT:")
        lines.append("-" * 80)
        lines.append("(A component's own structure is not a dependency between "
                     "components, so it does not belong in the graph)")
        for dep in results['self_dependencies']:
            lines.append(f"  - {dep['from']} -> {dep['to']}")
            lines.append(f"    Both belong to {dep['component']}")
        lines.append("")
    else:
        lines.append("OK: no dependencies declared within a component")
        lines.append("")
    # Unknown fields in the dependency blocks
    if results['unknown_fields']:
        lines.append("UNKNOWN FIELDS:")
        lines.append("-" * 80)
        lines.append("(Fields in a dependency block outside the recognised set: "
                      f"{', '.join(sorted(KNOWN_YAML_FIELDS))})")
        for warning in results['unknown_fields']:
            lines.append(f"  - {warning}")
        lines.append("")
    else:
        lines.append("OK: no unknown fields in dependency blocks")
        lines.append("")
    # Summary
    lines.append("=" * 80)
    total_issues = (len(results['cycles']) + len(results['disconnected'])
                    + len(results['invalid_refs']) + len(results['self_dependencies'])
                    + len(results['unknown_fields']))
    if total_issues == 0 and results['is_dag']:
        lines.append("VALIDATION PASSED - no issues found")
    else:
        lines.append(f"VALIDATION FAILED - {total_issues} issue(s) found")
    lines.append("=" * 80)
    report = '\n'.join(lines)
    if output_file:
        output_file.write_text(report, encoding='utf-8')
        print(f"Report written to: {output_file}")
    return report


def main():
    parser = argparse.ArgumentParser(
        description='Validate the capability dependency graph declared by component specifications'
    )
    parser.add_argument(
        '--specs-dir',
        type=Path,
        default=Path('docs/components'),
        help='Directory containing component specifications (default: docs/components)'
    )
    parser.add_argument(
        '--output',
        type=Path,
        help='Output file for validation report (default: print to stdout)'
    )
    args = parser.parse_args()
    if not args.specs_dir.exists():
        print(f"ERROR: Specifications directory not found: {args.specs_dir}", file=sys.stderr)
        sys.exit(1)
    print("Building dependency graph...")
    graph, file_map, all_capabilities, all_warnings = build_dependency_graph(args.specs_dir)
    print("Validating graph...")
    results = validate_graph(graph, all_capabilities, all_warnings)
    print("\nGenerating report...")
    report = generate_report(results, args.output)
    if not args.output:
        print("\n")
        print(report)
    # Exit with error code if validation failed. Disconnected nodes are reported but do
    # not fail the run — see the note at the top of this file.
    total_issues = (len(results['cycles']) + len(results['invalid_refs'])
                    + len(results['self_dependencies'])
                    + len(results['unknown_fields']))
    if not results['is_dag'] or total_issues > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main()
