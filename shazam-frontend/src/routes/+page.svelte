<script lang="ts">

    const siteInfo = {
    "name": "Webmatrices",
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
        <input type="text" placeholder="Search" />
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
    }
    .logo img {
        @apply h-8;
    }
    .exceptional-logo {
        @apply text-2xl font-bold;
        @apply first-letter:uppercase first-letter:font-extrabold;
        
        @apply first-letter:text-indigo-100 first-letter:bg-indigo-500;
        @apply dark:first-letter:text-indigo-500 dark:first-letter:bg-indigo-100;

        
        @apply bg-gradient-to-r from-indigo-500 to-sky-600 to-blue-700;
        @apply dark:from-indigo-700 dark:to-indigo-500;

        @apply bg-clip-text text-transparent;

        @apply first-letter:rounded-full first-letter:px-2;
        @apply first-letter:shadow-lg first-letter:transform first-letter:-rotate-6;
    }
    
</style>