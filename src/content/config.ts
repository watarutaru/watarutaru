import { defineCollection, z } from "astro:content";

const blog = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    category: z.string().optional(),
    tags: z.array(z.string()).default([]),
    description: z.string().optional(),
    thumbnail: z.string().optional(),
    originalUrl: z.string().optional(),
    sourceUrl: z.string().optional(),
    archivedAt: z.union([z.string(), z.number()]).optional(),
  }),
});

export const collections = { blog };