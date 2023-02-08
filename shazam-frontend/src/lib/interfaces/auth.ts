import type { GlobalResponse } from "$lib/interfaces";

export interface User {
    id: number
    first_name?: string
    last_name?: string
    email: string
    username: string
    is_staff?: string
    is_superuser?: string
    is_verified?: boolean
    status: Status
    profile: Profile
}

export interface Status {
    is_confirmed: boolean
    last_sent_time: string
    token_key_expires: string
}

export interface Profile {
    bio?: string
    location?: string
    birth_date?: string
    image?: string
}

export interface AuthResponse extends GlobalResponse {
    email: string[]
    username: string[]
    password: string[]
    password_confirmation: string[]
}

export interface ForgotUsernameResponse extends AuthResponse {
    type: string
}

export interface ForgotPasswordResponse extends AuthResponse {
    type?: string[]
    redirect?: boolean
    expired_token?: boolean
    invalid_token?: boolean
}

export interface ConfirmationResponse {
    time_left_in_minutes: number
    success: boolean
}