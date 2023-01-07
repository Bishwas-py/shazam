const config = {
	content: ['./src/**/*.{html,js,svelte,ts}'],

	theme: {
		extend: {
			fontFamily: {
				'play-fair': ['play-fair', 'sans-serif'],
				combo: ['combo', 'sans-serif'],
				lato: ['lato', 'sans-serif'],
				ssp: ['source-sans-pro', 'sans-serif'],
				inter: ['inter', 'sans-serif'],
				poppins: ['poppins', 'sans-serif'],
				ds: ['dancing-script', 'sans-serif']
			}
		}
	},

	plugins: []
};

module.exports = config;
