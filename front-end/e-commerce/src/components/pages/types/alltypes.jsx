import {DesktopBar} from '../../utils/nav/desktopBar'
import CarTypes from '../../utils/display/cartypes'
import DesktopFooter from '../../utils/nav/desktopFooter'
import MediaQuery from 'react-responsive'
import MobileBar from '../../utils/nav/mobileBar'

function AllTypes() {
  return (
    <main className='flex flex-col  min-h-[100vh] justify-between gap-6 font-main'>
      <MediaQuery minWidth={'801px'}>
         <DesktopBar />
      </MediaQuery>
      <MediaQuery maxWidth={'800px'}>
         <MobileBar />
      </MediaQuery>
      <div>
         <h3 className="text-blue-950 font-bold mb-4 ml-4 md:ml-8 lg:ml-14 text-2xl mt-16 md:mt-24 lg:mt-28">
            Browse by Category
         </h3>
         <CarTypes />
      </div>
      <DesktopFooter />
    </main>
  )
}

export default AllTypes
