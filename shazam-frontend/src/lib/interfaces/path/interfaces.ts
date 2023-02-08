
export interface Home {
    main: string
}

export interface Auth {
    login: string,
    refresh: string,
    verify: string,

    register: string,
    user: string
    confirm_email: string,
    forgot_password: string,
    forgot_username: string,
}

export interface Path {
    index: Home,
    auth: Auth
}
