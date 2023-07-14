<script>
	import { faChevronDown } from '@fortawesome/free-solid-svg-icons';
	import Fa from 'svelte-fa';
</script>

<div class="nav-top-container">
	<div class="nav-section">
		<a href="#" class="nav-item">My Feed</a>
		<a href="#" class="nav-item">Explore</a>
		<a href="#" class="nav-item">Bookmarks</a>
		<div class="relative">
			<button class="nav-item">More <Fa icon={faChevronDown} /></button>
			<div class="nav-drop-section">
				<a href="#" class="nav-drop-item">Settings</a>
				<a href="#" class="nav-drop-item">Help</a>
				<a href="#" class="nav-drop-item">Keyboard Shortcuts</a>
				<a href="#" class="nav-drop-item">Log Out</a>
			</div>
		</div>
	</div>
</div>

<style lang="postcss">
    .nav-top-container {
        @apply flex flex-row items-center justify-center w-full;
        @apply font-inter;
    }
	.nav-section {
		@apply flex flex-row items-center justify-center;
		@apply h-full;
	}

	.nav-item {
		@apply text-gray-600;
		@apply text-sm;
		@apply font-semibold;
		@apply py-2;
		@apply px-4;
		@apply hover:bg-gray-100 hover:text-gray-800 hover:outline hover:outline-1 hover:outline-gray-200;
		@apply rounded-full;
        @apply flex gap-3 items-center;
	}

	.nav-drop-section {
		@apply absolute;
		@apply top-0;
		@apply left-0;
		@apply mt-10;
		@apply w-48;
		@apply bg-white;
		@apply border border-gray-200;
		@apply rounded-lg;
		@apply shadow-md;
		@apply hidden;
	}

	.nav-drop-item {
		@apply block;
		@apply text-gray-600;
		@apply text-sm;
		@apply font-semibold;
		@apply py-2;
		@apply px-4;
		@apply hover:bg-gray-100 hover:text-gray-800;
	}
</style>
