<script lang="ts">
    import Fa from 'svelte-fa';
    import {faSearch} from "@fortawesome/free-solid-svg-icons";
    import {page} from "$app/stores";
    import Logo from "$items/Logo.svelte";
</script>

<nav>
    <Logo/>
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