import { defineCollection, z } from "astro:content";

const blog = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string(),
    date: z
      .union([z.string(), z.date(), z.number()])
      .transform((v) => (v instanceof Date ? v : new Date(v))),
  }),
});

export const collections = { blog };