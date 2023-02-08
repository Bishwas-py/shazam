import type {SiteData} from "$lib/interfaces/site";

export interface MainContext {
    siteData: SiteData
}

export interface GlobalResponse {
    detail: string[]
    invalid: string[]
    message: string[]
    error: string[]
}
