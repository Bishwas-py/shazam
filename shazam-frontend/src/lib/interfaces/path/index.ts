import type {Path} from "./interfaces";
import {SECRET_BASE_URL} from '$env/static/private';

export function makeAPIPath(path: string): string {
    return SECRET_BASE_URL + path;
}


export const apiPath: Path = {
    index: {
        main: makeAPIPath('/'),
    },
    auth: {
        login: makeAPIPath('/auth/login/'),
        refresh: makeAPIPath('/auth/refresh/'),
        verify: makeAPIPath('/auth/verify/'),

        register: makeAPIPath('/auth/register/'),
        user: makeAPIPath('/auth/user/'),
        confirm_email: makeAPIPath('/auth/confirm-email/'),
        forgot_password: makeAPIPath('/auth/forgot-password/'),
        forgot_username: makeAPIPath('/auth/forgot-username/'),
    },
}
