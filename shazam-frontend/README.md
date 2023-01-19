## For contributor
In the `shazam/shazam-frontend/svelte.config.js` you will have four aliases; `$item`, `$fonts`, `$utils` and `$root`

```
kit: {
  adapter: adapter(),
  alias: {
    $item: './src/item',
    $fonts: './src/fonts',
    $utils: './src/utils',
    $root: './src'
  }
}
```

As mentioned by the original auther, here are their purposes:

- `$items` is used to put Svelte components
- `$fonts` is used to put custom font dependencies/files
- `$utils` is for quick functions, utils i.e. validators.
- `$root` can be used if you wanna access the stuff inside `src/` quickly

And as we all know `$lib` is not mentioned here. Feel free to use `$lib` as well, just mention the purpose of using it while the pull request.
