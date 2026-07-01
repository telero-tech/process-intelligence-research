# process-intelligence-research

Exploration of [Process Intelligence Research](https://www.pi-research.org/) graph serialization tools for flowsheets and P&IDs.

## GGILES

[GGILES](https://github.com/process-intelligence-research/Generalized-graph-line-entry-system) (Generalized Graph Input Line Entry System) converts between NetworkX graphs and compact string representations. It supports typed nodes and edges, attributes, cycles, branches, and canonical sequences for graph comparison.

This repo includes `ggiles_quickstart.py`, a runnable version of the package README quickstart.

```bash
uv sync
uv run python ggiles_quickstart.py
```

## SFILES2

[SFILES2](https://github.com/process-intelligence-research/SFILES2) is the domain-specific counterpart: it converts process flow diagrams (PFDs) and piping & instrumentation diagrams (P&IDs) between NetworkX flowsheet graphs and [SFILES 2.0](https://link.springer.com/article/10.1007/s11081-023-09798-9) strings. It also supports rendering flowsheet diagrams from graph data.

GGILES generalizes the ideas behind SFILES 2.0 to arbitrary typed graphs; SFILES2 applies a fixed flowsheet vocabulary and PFD/P&ID visualization.

Neither package reads image files (e.g. PNG/PDF scans) directly — both expect a structured graph or an existing string representation.
