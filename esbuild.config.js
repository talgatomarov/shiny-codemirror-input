const esbuild = require("esbuild");

esbuild
  .build({
    entryPoints: ["./src/index.js"],
    outfile: "./shiny_codemirror_input/distjs/index.js",
    bundle: true,
    minify: true,
    target: ["es2020"],
    platform: "browser",
  })
  .catch(() => process.exit(1));
