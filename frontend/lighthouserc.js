module.exports = {
    ci: {
      collect: {
        url: [
          'http://localhost:5173',
        ],
        startServerCommand: 'npm run dev',
      },
      assert: {
        assertions: {
          /* Warnings */
          "categories:performance": ["warn", {"minScore": 0.9}],

          /* Errors */
          "categories:performance": ["error", {"minScore": 0.5}],
          "categories:accessibility": ["error", {"minScore": 0.9}],
          "categories:best-practices": ["error", {"minScore": 0.9}],
          "categories:seo": ["error", {"minScore": 0.9}],
        },
      },
      upload: {
        target: 'temporary-public-storage',
      },
    },
  };