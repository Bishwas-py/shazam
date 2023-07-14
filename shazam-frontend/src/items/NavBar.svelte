<script lang="ts">
    import Fa from 'svelte-fa';
    import {faChevronDown} from "@fortawesome/free-solid-svg-icons";
    import Logo from "$items/Logo.svelte";
    import NavSection from "$items/NavSection.svelte";
</script>

<nav>
    <Logo/>

    <!-- Add a responsive bar containing: My Feed, Explore, Bookmarks, More (dropdown) -->
    <!-- In More: Settings, Help, Keyboard Shortcuts, Log Out -->
    <NavSection/>


</nav>
<style lang="postcss">
    nav {
        @apply bg-white dark:bg-gray-800;
        @apply border-b border-gray-200 dark:border-gray-700;
        @apply flex items-center justify-between;
        @apply px-4 py-4 sm:px-6 lg:px-16;
    }
</style>