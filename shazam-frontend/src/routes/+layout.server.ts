import type {LayoutServerLoad} from './$types';
import type {SiteData} from "$lib/interfaces/site";
import {apiPath} from "$lib/interfaces/path";

const getSiteData = async (): Promise<SiteData> => {
    const response = await fetch(apiPath.index.main);
    return await response.json();
}
export const load: LayoutServerLoad = async ({fetch}) => {
    const siteInfo = await getSiteData();
    console.log(siteInfo);
    return {
        siteInfo,
    }
}
