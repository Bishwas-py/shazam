<script lang="ts">
	import { page } from '$app/stores';
	$: ({ GetSiteInfo } = $page.data);
	$: ({ siteInfo } = $GetSiteInfo.data);
</script>

<a class="logo" href="/">
	{#if siteInfo?.logo}
		<img src={siteInfo?.logo} alt={siteInfo?.name} />
	{:else}
		<div class="exceptional-logo">
			{siteInfo?.name[0] +
				siteInfo?.name.slice(1, 11)}{#if siteInfo?.name.length > 11}.{/if}
		</div>
	{/if}
</a>

<style lang="postcss">
	.logo {
		@apply flex items-center;
		@apply shrink-0;
		@apply min-w-[300px];
	}
	.logo img {
		@apply h-8;
	}
	.exceptional-logo {
		@apply font-ds;
		@apply text-3xl font-bold;
		@apply first-letter:uppercase first-letter:font-extrabold;

		@apply text-slate-900 dark:text-slate-300;

		@apply first-letter:bg-gradient-to-r first-letter:from-indigo-500 to-sky-600 first-letter:to-blue-700;
		@apply dark:from-indigo-700 dark:to-indigo-500;

		@apply first-letter:bg-clip-text first-letter:text-transparent;
	}
</style>
