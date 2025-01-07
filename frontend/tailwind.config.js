/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        background: 'hsl(var(--background))',
        primary: 'hsl(var(--primary))',
        secondary: 'hsl(var(--secondary))',
        spotify: 'hsl(var(--spotify))',
      },
      animation: {
        'fade-in': 'fade-in 1s ease-out forwards',
      },
    },
  },
  plugins: [],
};