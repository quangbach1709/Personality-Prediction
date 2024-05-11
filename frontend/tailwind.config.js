/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      backgroundColor: {
        antiquewhite: 'antiquewhite',
        wheat: 'wheat',
      },
      width: {
        '80vw': '80vw',
        '70vw': '70vw',
        '60vw': '60vw'
      },
      translate: {
        'center': '-50%',
      }
    },
  },
  plugins: [],
}