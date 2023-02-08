<script lang="ts">
    import {page} from "$app/stores";
</script>

<div class="logo">
    {#if $page.data.siteInfo?.logo}
        <img src={$page.data.siteInfo?.logo} alt={$page.data.siteInfo?.name} />
    {:else}
        <div class="exceptional-logo">
            {$page.data.siteInfo?.name[0] + $page.data.siteInfo?.name.slice(1, 11)}{#if $page.data.siteInfo?.name.length > 11}.{/if}
        </div>
    {/if}
</div>


<style>
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
</style>