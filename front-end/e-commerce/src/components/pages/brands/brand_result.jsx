import MediaQuery from "react-responsive"
import DesktopFooter from "../../utils/nav/desktopFooter"
import { DesktopBar } from "../../utils/nav/desktopBar"
import MobileBar from "../../utils/nav/mobileBar"
import BrandSearch from "./brand_search"

function Brand() {
   let searchBrand = JSON.parse(localStorage.getItem('searchBrand'))
  return (
   <main className='flex flex-col gap-6 min-h-[100vh] justify-between font-main'>
      <MediaQuery minWidth={'801px'}>
         <DesktopBar />
      </MediaQuery>
      <MediaQuery maxWidth={'800px'}>
         <MobileBar />
      </MediaQuery>
   <div>
      <h3 className="text-blue-950 font-bold mb-4 ml-4 md:ml-8 lg:ml-14 text-2xl mt-16 md:mt-28 lg:mt-2">
         {searchBrand} cars....
      </h3>
      <BrandSearch />
   </div>
   <DesktopFooter />
   </main>
  )
}

export default Brand
