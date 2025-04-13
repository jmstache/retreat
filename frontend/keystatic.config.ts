import { config } from 'keystatic'

export default config({
  storage: {
    kind: 'local',
  },
  collections: {
    blog: {
      label: 'Blog Posts',
      path: 'content/blog/',
      schema: {
        title: { type: 'text', label: 'Title' },
        date: { type: 'datetime', label: 'Publish Date' },
        author: { type: 'text', label: 'Author' },
        body: { type: 'markdown', label: 'Content' },
        featuredImage: { type: 'url', label: 'Featured Image URL' }
      }
    }
  }
})
