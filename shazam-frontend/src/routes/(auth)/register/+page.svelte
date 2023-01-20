<svelte:head>
    <title>Shazam Blog | Register</title>
</svelte:head>
<section id="register" class="w-screen h-screen grid md:grid-cols-[55vw,45vw]">
    <div id="register-form-container" class="px-4 py-5 md:px-10 md:py-20 flex flex-col gap-y-5 md:gap-y-10">
        <div id="presentation-text-container" class="flex flex-col gap-y-2">
            <h1 class="text-3xl font-semibold">Welcome to the <span class="underline text-blue-600">Shazam</span> Community</h1>
            <h2>Create a network of friend and share your experiences</h2>
        </div>

        <form method="post" id="registering-form" class="w-full flex flex-col gap-y-10 max-w-[640px]">
            <label for="" class="flex flex-col gap-y-2">
                Enter your email address:
                <input type="email" name="email" id="" class="w-full h-12 border rounded px-2" placeholder="Ex: user@example.com">
            </label>

            <label for="" class="flex flex-col gap-y-2">
                Enter your username:
                <input type="text" name="username" id="" class="w-full h-12 border rounded px-2" placeholder="Ex: IamAWebDev">
            </label>

            <label for="" class="flex flex-col gap-y-2">
                Enter your password:
                <input type="password" name="password" id="" class="w-full h-12 border rounded px-2" placeholder="********">
                <span class="text-xs text-[#00000050]">*Your password must have at least: 8 characters, one uppercase, one lowercase, one special character, one number:</span>
            </label>

            <div id="actions-button-container" class="flex flex-col gap-y-4">
                <button class="text-white rounded-full w-[300px] bg-blue-600 h-12">Create my account</button>
                <span class="text-sm">You already have an account ? <a href="/login" class="underline text-blue-600">Sign In</a></span>
            </div>
        </form>
    </div>
    <div id="register-banner-container" class="hidden relative md:flex h-full">
        <div id="shadow" class="absolute top-0 left-0 w-full h-full z-10 bg-[#00000080]" />
        <img src="/images/register-banner.jpg" alt="" class="w-full h-full z-0 object-cover">
    </div>    
</section>

<style>
    *{
        font-family: poppins;
    }
</style>