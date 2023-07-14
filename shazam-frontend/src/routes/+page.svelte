<script lang="ts">
	import Fa from 'svelte-fa';
	import { faSearch } from '@fortawesome/free-solid-svg-icons';
	import { page } from '$app/stores';
	import type { PageData } from './$houdini';
	import { graphql } from '$houdini';

	export let data: PageData;
	$: ({ GetAllTenPosts } = data);
	$: ({allPosts} = $GetAllTenPosts.data);

</script>

<div class="article-container">
	{#each allPosts.edges as {node}}
	    <div class="article-card">
	        <div class="card-body">
	            <h5 class="card-title">{node.title}</h5>
	            <p class="card-text">{node.body}</p>
	            <a href="{node.trueSlug}" class="btn btn-primary">Go somewhere</a>
	        </div>
	    </div>
	{/each}
</div>

<style>
	.article-container {
		@apply grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4;
		@apply p-16;
		@apply font-inter;
	}
	.article-card {
		@apply border border-gray-200 rounded-lg shadow-md;
		@apply p-4;
		@apply mb-4;
		@apply bg-white hover:bg-gray-50;
		@apply hover:shadow-lg;
	}

	.card-body {
		@apply p-4;
	}

	.card-title {
		@apply text-2xl;
		@apply font-bold;
		@apply mb-4;
	}

	.card-text {
		@apply text-gray-500;
		@apply mb-4;
	}

	.btn {
		@apply bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded;
	}
</style>
