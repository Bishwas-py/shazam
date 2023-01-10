<script lang="ts">
    import Fa from 'svelte-fa';
    import {faSearch} from "@fortawesome/free-solid-svg-icons";

    const siteInfo = {
    "name": "Shazam Blog",
    "description": "A blog developed with Django and SvelteKit",
    "author": "Bishwas-py",
    "domain": "shazam.blog",
    "url": "https://shazam.blog",
    "logo": "",
    "email": "",
    "social": [
        {
            "name": "twitter",
            "url": "https://twitter.com/bhBishwas",
            "icon": "https://twitter.com/favicon.ico"
        },
        {
            "name": "github",
            "url": "https://github.com/bishwas-py",
            "icon": "https://github.com/favicon.ico"
        }
    ]
};
</script>

<nav>
    <div class="logo">
        {#if siteInfo.logo}
            <img src={siteInfo.logo} alt={siteInfo.name} />
        {:else}
            <div class="exceptional-logo">
                {siteInfo.name[0] + siteInfo.name.slice(1, 11)}{#if siteInfo.name.length > 11}.{/if}
            </div>
        {/if}
    </div>
    <!-- search box -->
    <div class="search-box">
        <small>
            <Fa icon="{faSearch}"/>
        </small>
        <input type="text" placeholder="Search" />
        <span>/</span>
    </div>
    
</nav>

<style>
    nav {
        @apply bg-white dark:bg-gray-800;
        @apply border-b border-gray-200 dark:border-gray-700;
        @apply flex items-center justify-between;
        @apply px-4 py-4;
    }
    .logo {
        @apply flex items-center;
        @apply shrink-0;
        @apply min-w-[300px];
    }
    .logo img {
        @apply h-8;
    }
    .exceptional-logo {
        @apply text-2xl font-bold;
        @apply first-letter:uppercase first-letter:font-extrabold;
        
        @apply text-slate-900 dark:text-slate-300;
        
        @apply first-letter:bg-gradient-to-r first-letter:from-indigo-500 to-sky-600 first-letter:to-blue-700;
        @apply dark:from-indigo-700 dark:to-indigo-500;

        @apply first-letter:bg-clip-text first-letter:text-transparent;
    }

    .search-box {
        @apply flex items-center;
        @apply bg-gray-100 dark:bg-gray-700;
        @apply rounded-full;
        @apply px-2 py-1;
        @apply text-gray-500 dark:text-gray-400;
        @apply w-full;
        @apply h-11;
    }

    .search-box small {
        @apply flex items-center;
        @apply text-gray-500 dark:text-gray-400;
        @apply mr-2;
    }
    .search-box input {
        @apply bg-transparent;
        @apply border-none;
        @apply outline-none;
        @apply text-sm;
        @apply text-gray-700 dark:text-gray-300;
        @apply w-full;
    }
    .search-box span {
        @apply text-gray-500 dark:text-gray-400;
        @apply bg-slate-50 dark:bg-slate-900;
        @apply rounded-md;
        @apply px-1 py-0.5;
    }
</style>