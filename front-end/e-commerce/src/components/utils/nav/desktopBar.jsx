import { Link } from 'react-router-dom'
import { useEffect, useState } from 'react';
import MediaQuery from 'react-responsive';

function HomeDesktopBar() {
   const [isScrolled, setIsScrolled] = useState(false)
   useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 0)
      }
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);
  return (
   <nav className={`flex justify-between text-white items-center w-full fixed py-2 md:py-5 z-10 border-b border-b-white px-4 md:px-8 lg:px-12 ${isScrolled ? 'bg-white text-blue-950 shadow-xl' : ''}`}>
      <Link to={'/'} className={`font-semibold text-xl ${isScrolled ? 'text-blue-950' : ''}`}>
         MACELO AUTO<small className='text-xs'>s</small>
      </Link>
         <ul className='text-md font-medium flex gap-5 items-center'>
            <li className={`hover:text-blue-500 text-xs font-semibold  ${isScrolled ? 'hover:text-blue-600 text-blue-950' : ''}`}>
               <Link to={'/featured'}>Inventory</Link>
            </li>
            <li className={`hover:text-blue-500 text-xs font-semibold  ${isScrolled ? 'hover:text-blue-600 text-blue-950' : ''}`}>
               <Link to={'/find'}>
                  Find a Car
               </Link>
            </li>
            <li className={`hover:text-blue-500 text-xs font-semibold  ${isScrolled ? 'hover:text-blue-600 text-blue-950' : ''}`}>
               <Link>
                  Shopping Cart
               </Link>
            </li>
            <li className={`hover:text-blue-500  text-xs font-semibold  ${isScrolled ? 'hover:text-blue-600 text-blue-950' : ''}`}>
               <Link onClick={() => {
                  window.scrollTo({
                     top: document.documentElement.scrollHeight,
                     behavior: "smooth"
                  });
               }}>Contact Us</Link>
            </li>
         </ul>
   </nav>
  )
}






function DesktopBar() {
   const [isScrolled, setIsScrolled] = useState(false)

   useEffect(() => {
      const handleScroll = () => {
         setIsScrolled(window.scrollY > 0)
      }
      window.addEventListener('scroll', handleScroll)
      return () => window.removeEventListener('scroll', handleScroll)
   })

  return (
   <nav className={`flex justify-between items-center w-full fixed py-5 z-10 text-blue-950  border-b border-b-blue-950 px-4 md:px-8 lg:px-12 ${isScrolled ? 'shadow-xl border-b-0 bg-white' : 'bg-blue-950 text-white'}`}>
      <Link to={'/'} className={`font-semibold text-xl ${isScrolled ? 'text-blue-950' : ''}`}>
         MACELO AUTO<small className='text-xs'> s</small>
      </Link>
      <MediaQuery minWidth={'767px'} >
         <ul className='text-md font-medium flex gap-5 items-center'>
            <li className={`hover:text-blue-500 text-xs font-semibold  ${isScrolled ? 'hover:text-blue-600 text-blue-950' : ''}`}>
               <Link to={'/featured'}>Inventory</Link>
            </li>
            <li className={`hover:text-blue-500 text-sm font-semibold  ${isScrolled ? 'hover:text-blue-600 text-blue-950' : ''}`}>
               <Link to={'/find'}>
                  Find a Car
               </Link>
            </li>
            <li className={`hover:text-blue-500 text-xs font-semibold  ${isScrolled ? 'hover:text-blue-600 text-blue-950' : ''}`}>
               <Link>
                  Shopping Cart
               </Link>
            </li>
            <li className={`hover:text-blue-500  text-xs font-semibold  ${isScrolled ? 'hover:text-blue-600 text-blue-950' : ''}`}>
               <Link onClick={() => {
                  window.scrollTo({
                     top: document.documentElement.scrollHeight,
                     behavior: "smooth"
                  });
               }}>Contact Us</Link>
            </li>
         </ul>
      </MediaQuery>
   </nav>
  )
}

export { DesktopBar, HomeDesktopBar}
