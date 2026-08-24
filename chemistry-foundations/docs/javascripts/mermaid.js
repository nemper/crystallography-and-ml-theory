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
  }
});
