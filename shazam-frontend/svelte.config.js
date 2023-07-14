import preprocess from 'svelte-preprocess';
import adapter from '@sveltejs/adapter-auto';
import {vitePreprocess} from '@sveltejs/kit/vite';

/** @type {import('@sveltejs/kit').Config} */
const config = {
    // Consult https://kit.svelte.dev/docs/integrations#preprocessors
    // for more information about preprocessors
    preprocess: [
        vitePreprocess(),
        preprocess({
            postcss: true
        })
    ],

    kit: {
        adapter: adapter(),
        alias: {
            $root: './src',
            $fonts: './src/fonts',
            $utils: './src/utils',
            $items: './src/items',
            $houdini: './$houdini',
        }
    }
};

export default config;
