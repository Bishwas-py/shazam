import houdini from 'houdini/vite'
import {sveltekit} from "@sveltejs/kit/vite";

/** @type {import('vite').UserConfig} */
const config = {
	plugins: [houdini(), sveltekit()],
	test: {
		include: ['src/**/*.{test,spec}.{js,ts}']
	}
};

export default config;
