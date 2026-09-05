window.MathJax = {
  startup: {
    typeset: false,
    // Source formulas are TeX; assistive MathML is output, not a second input.
    input: ["tex"],
    ready() {
      MathJax.startup.defaultReady();

      let pending = MathJax.startup.promise;
      let previousContent = null;

      document$.subscribe(() => {
        const content = document.querySelector(".md-content__inner");

        pending = pending
          .then(async () => {
            if (!content?.isConnected || content === previousContent) return;

            // Forget the removed page only; never clear and rescan the same page.
            MathJax.typesetClear();
            MathJax.texReset();
            MathJax.startup.output.clearCache();
            await MathJax.typesetPromise([content]);
            previousContent = content;
          })
          .catch((error) => console.error("MathJax typesetting failed:", error));
      });
    },
  },
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex",
  },
};
