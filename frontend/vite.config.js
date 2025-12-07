import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    // Output directory for built files
    outDir: '../backend/static',
    // Clear output directory before each build
    emptyOutDir: true,
    // Generate manifest for Django integration
    manifest: true,
    rollupOptions: {
      // Define entry point
      input: 'src/main.jsx',
    },
  },
  server: {
    // Development server port
    port: 3000,
    // Enable hot module replacement
    hmr: true,
    // Proxy API requests to Django during development
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
})