import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "Study Wiki",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "en-US",
    // GitHub Pages project site URL (https://maxwernz.github.io/study-wiki/).
    baseUrl: "maxwernz.github.io/study-wiki",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        // Academic / serif look: Baskerville headings over a Lora reading face.
        header: "Libre Baskerville",
        body: "Lora",
        code: "IBM Plex Mono",
      },
      colors: {
        lightMode: {
          light: "#fbf9f4", // warm paper background
          lightgray: "#e6e0d4", // rules & borders
          gray: "#9c9382", // muted text, graph links
          darkgray: "#33312c", // body text
          dark: "#1a1814", // headings
          secondary: "#7d1f35", // deep maroon accent (links, active)
          tertiary: "#b08544", // muted gold (hover, graph nodes)
          highlight: "rgba(125, 31, 53, 0.08)", // internal-link background
          textHighlight: "#e9d8a688", // marker highlight
        },
        darkMode: {
          light: "#1a1815", // warm near-black background
          lightgray: "#3a362f",
          gray: "#6f685b",
          darkgray: "#d8d2c4", // body text
          dark: "#f0eadd", // headings
          secondary: "#d98a9e", // soft rose accent for dark mode
          tertiary: "#c8a86a", // gold
          highlight: "rgba(217, 138, 158, 0.10)",
          textHighlight: "#b3aa0288",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
