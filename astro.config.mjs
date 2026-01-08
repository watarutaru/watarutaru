// @ts-check
import { defineConfig } from 'astro/config';
import remarkAttr from 'remark-attr';

// https://astro.build/config
export default defineConfig({
  markdown: {
    remarkPlugins: [remarkAttr],
  },
});
