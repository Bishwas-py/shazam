<script lang="ts">
    import '$fonts/styles/play-fair.css';
    import '$fonts/styles/combo.css';
    import '$fonts/styles/lato.css';
    import '$fonts/styles/source-sans-pro.css';
    import '$fonts/styles/inter.css';
    import '$fonts/styles/dancing-script.css';
    import '$fonts/styles/poppins.css';
    import '../styles/app.postcss';
    import NavBar from "$items/NavBar.svelte";
    import type { PageData } from "./$houdini";

    export let data: PageData;
    $: ({ GetSiteInfo } = data);
    $: ({ siteInfo } = $GetSiteInfo.data);
</script>

<svelte:head>
    <title>{siteInfo.name}</title>
    <meta name="description" content={siteInfo.description} />
</svelte:head>
<NavBar />
<slot />