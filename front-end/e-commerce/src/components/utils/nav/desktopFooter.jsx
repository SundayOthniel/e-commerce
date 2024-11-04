import { FaTwitter, FaInstagram, FaFacebook, FaLinkedin } from "react-icons/fa";
import { Link } from "react-router-dom";

function DesktopFooter() {
  return (
   <footer  className=" overflow-hidden flex flex-col gap-5 px-14 items-center bg-blue-950 text-white font-price pt-10 justify-center">
      <div className="flex gap-2 items-center">
         <div className="h-[2px] bg-white w-[50vw]"></div>
         <ul className="flex gap-3">
            <li className="flex text-xs items-center gap-2">
               <Link to='/'>
                  <FaTwitter className="w-5 h-5" />
               </Link>
            </li>
            <li className="flex text-xs items-center gap-2">
               <Link to='/'>
                  <FaInstagram className="w-5 h-5"/>
               </Link>
            </li>
            <li className="flex text-xs items-center gap-2">
               <Link to='/'>
                  <FaFacebook className="w-5 h-5"/>
               </Link>
            </li>
            <li className="flex text-xs items-center gap-2">
               <Link to='/'>
                  <FaLinkedin className="w-5 h-5" />
               </Link>
            </li>
         </ul>
         <div className="h-[2px] bg-white w-[50vw]"></div>
      </div>
      <h5 className='font-normal md:text-xl'>
         MACELO AUTO<small className='text-[9px]'>s</small>
      </h5>
      <p className="text-[9px] pb-2">
         Copyright © 2024 Macelo Auto's.
      </p>
   </footer> 
  )
}

export default DesktopFooter
