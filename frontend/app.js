document.getElementById("search").addEventListener("input", async (e) => {
  const q = e.target.value;
  const res = await fetch("http://localhost:8000/search", {
    method: "POST",
    body: JSON.stringify({ query: q }),
    headers: { "Content-Type": "application/json" },
  });
  const data = await res.json();
  render(data);
});

function render(snippets) {
  const div = document.getElementById("results");
  div.innerHTML = "";
  snippets.forEach(s => {
    const pre = document.createElement("pre");
    pre.innerText = `// ${s.title} (${s.language})\n${s.code}`;
    div.appendChild(pre);
  });
}
