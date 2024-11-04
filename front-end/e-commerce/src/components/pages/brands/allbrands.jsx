import React from 'react'
import {DesktopBar} from '../../utils/nav/desktopBar'
import CarBrands from '../../utils/display/carbrands'
import MobileBar from '../../utils/nav/mobileBar'
import DesktopFooter from '../../utils/nav/desktopFooter'
import MediaQuery from 'react-responsive'

function AllBrands() {
  return (
    <main className='flex flex-col gap-6 min-h-[100vh] justify-between font-main'>
      <MediaQuery minWidth={'801px'}>
         <DesktopBar />
      </MediaQuery>
      <MediaQuery maxWidth={'800px'}>
         <MobileBar />
      </MediaQuery>
      <div>
         <h3 className="text-blue-950 font-bold mb-4 ml-4 md:ml-8 lg:ml-14 text-2xl mt-16 md:mt-24 lg:mt-28">
            Explore Our Premium Brands
         </h3>
         <CarBrands />
      </div>
      <DesktopFooter />
    </main>
  )
}

export default AllBrands
