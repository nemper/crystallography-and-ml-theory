mermaid.initialize({
  startOnLoad: false,
  securityLevel: "strict",
  theme: "base",
  themeVariables: {
    background: "#ffffff",
    primaryColor: "#eef2ff",
    primaryTextColor: "#111827",
    primaryBorderColor: "#4f46e5",
    lineColor: "#64748b",
    secondaryColor: "#ecfeff",
    tertiaryColor: "#f8fafc",
    noteBkgColor: "#fef3c7",
    noteTextColor: "#111827",
  },
});

document$.subscribe(async () => {
  const nodes = [];

  document.querySelectorAll("pre.mermaid-course").forEach((source) => {
    const diagram = document.createElement("div");
    diagram.className = "mermaid-course";
    diagram.textContent = source.textContent;
    source.replaceWith(diagram);
    nodes.push(diagram);
  });

  if (nodes.length > 0) {
    await mermaid.run({ nodes });

    nodes.forEach((diagram) => {
      const svg = diagram.querySelector("svg");
      const width = svg?.viewBox.baseVal.width;

      if (Number.isFinite(width) && width > 0) {
        // Preserve Mermaid's font size instead of shrinking wide diagrams.
        svg.style.width = `${width}px`;
        svg.style.maxWidth = "none";
      }

      diagram.tabIndex = 0;
      diagram.setAttribute("role", "region");
      diagram.setAttribute(
        "aria-label",
        "Dijagram. Širi sadržaj možete pomerati strelicama ulevo i udesno.",
      );
    });
  }
});
