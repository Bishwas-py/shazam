<svelte:head>
    <title>Shazam Blog | Register</title>
</svelte:head>

<section id="register">
    <div id="register-form-container">
        <div id="presentation-text-container">
            <h1>Welcome to the <span id="shazam-text">Shazam</span> Community</h1>
            <h2>Create a network of friend and share your experiences</h2>
        </div>
        <form method="post" id="registering-form">
            <label for="email">
                Enter your email address:
                <input type="email" name="email" id="email" placeholder="Ex: user@example.com">
            </label>

            <label for="username">
                Enter your username:
                <input type="text" name="username" id="username" placeholder="Ex: IamAWebDev">
            </label>

            <label for="password">
                Enter your password:
                <input type="password" name="password" id="password" placeholder="********">
                <span id="password-info">*Your password must have at least: 8 characters, one uppercase, one lowercase, one special character, one number:</span>
            </label>

            <div id="actions-button-container">
                <button type="submit">Create my account</button>
                <p>You already have an account ? <a href="/login">Sign In</a></p>
            </div>
        </form>
    </div>
    <div id="register-banner-container">
        <div id="shadow" />
        <img src="/images/register-banner.jpg" alt="banner-register">
    </div>    
</section>

<style>
    *{
        @apply font-inter;
    }

    section {
        @apply w-screen h-screen grid md:grid-cols-[55vw,45vw]
    }
    #register-form-container {
        @apply px-4 md:px-10 md:py-20 flex flex-col gap-y-5 md:gap-y-10
    }
    #presentation-text-container {
        @apply flex flex-col gap-y-2
    }
    #presentation-text-container h1 {
        @apply text-3xl font-semibold
    }
    #shazam-text {
        @apply underline text-blue-600
    }
    form {
        @apply w-full flex flex-col gap-y-10 max-w-[640px]
    }
    form input {
        @apply w-full h-12 border rounded px-2
    }
    form label {
        @apply flex flex-col gap-y-2
    }
    #password-info {
        @apply text-xs text-[#00000050]
    }
    #actions-button-container {
        @apply flex flex-col gap-y-4
    }
    #actions-button-container > button {
        @apply text-white rounded-full w-[300px] bg-blue-600 h-12
    }
    #actions-button-container p {
        @apply text-sm
    }

    #actions-button-container a {
        @apply underline text-blue-600
    }

    #register-banner-container {
        @apply hidden relative md:flex h-full
    }
    #shadow {
        @apply absolute top-0 left-0 w-full h-full z-10 bg-[#00000080]
    }
    #register-banner-container img {
        @apply w-full h-full z-0 object-cover
    }
</style>