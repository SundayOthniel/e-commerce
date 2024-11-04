import "react-responsive-carousel/lib/styles/carousel.min.css"
import { Carousel } from 'react-responsive-carousel'
import { HomeDesktopBar } from '../utils/nav/desktopBar'
import Search from '../utils/search'
import MediaQuery from 'react-responsive'
import { MdArrowOutward } from "react-icons/md";
import { Link } from "react-router-dom"
import Box from "../utils/display/box"
import CarBrands from "../utils/display/carbrands"
import CarTypes from "../utils/display/cartypes"
import { useRef, useEffect, useState } from "react"
import Listin from "../utils/display/listings"
import DesktopFooter from "../utils/nav/desktopFooter"
import MobileBar from "../utils/nav/mobileBar"
import { EncodeCars } from "../utils/carData/cars"

function Home() {
   const slides = [
      {image: `w14.webp`},
      {image: "w15.webp"},
      {image: "w16.webp"},
      {image: "w17.webp"},
   ]
   const imageRef = useRef(null);
   const containerRef = useRef(null);
   const [containerWidth, setContainerWidth] = useState(0);

  useEffect(() => {
    const handleResize = () => {
      if (containerRef.current) {
        const newWidth = containerRef.current.clientWidth;
        setContainerWidth(newWidth);
      
      }
    };

    window.addEventListener('resize', handleResize);

    return () => window.removeEventListener('resize', handleResize);
  }, [])

  useEffect(() => {EncodeCars()}, [])

  useEffect(() => {
      if (containerRef.current) {
        const newWidth = containerRef.current.clientWidth;
        setContainerWidth(newWidth);
      }
  })

  useEffect(() => {
    if (imageRef.current && containerWidth > 0) {
      const image = imageRef.current;
      const newHeight = containerWidth / (image.naturalWidth / image.naturalHeight);
      containerRef.current.style.height = `${newHeight}px`;
    }
  }, [containerWidth]); 


  return (
   <main className='overflow-hidden flex flex-col font-main gap-6 md:md-10 lg:gap-14' >
      <MediaQuery minWidth={'801px'}>
         <HomeDesktopBar />
      </MediaQuery>
      <MediaQuery maxWidth={'800px'}>
         <MobileBar home={true}/>
      </MediaQuery>
      <Carousel 
         infiniteLoop useKeyboardArrows autoPlay stopOnHover={true} showIndicators={false} transitionTime={'1000'} showThumbs={false} showArrows={false} showStatus={false} interval={'6000'}>
         {
            slides.map((slide) => (
               <div 
                  className='relative ' key={slide.image}>
                  <img 
                     src={`/e-commerce_project/components/pages/desktop/${slide.image}`} ref={imageRef} 
                     srcSet={`/e-commerce_project/components/pages/mobile/${slide.image} 300w, /e-commerce_project/components/pages/tablet/${slide.image} 600w, /e-commerce_project/components/pages/desktop/${slide.image} 1200w`} 
                     sizes="(max-width: 600px) 300px, (max-width: 1200px) 600px, 1200px"
                     alt="Background Image" 
                     rel="preload" 
                     fetchpriority="high"
                     />
               </div>               
            ))
         }
      </Carousel>
      <div ref={containerRef} className="w-[100%] bg-[rgba(0,0,0,0.5)] absolute top-0">

      </div>
      <section 
         className='absolute top-[8%] md:top-[15%] flex-col w-full flex box-border lg:px-12 md:px-8 px-4 gap-4 items-start'>
         <h1  
            className='text-white text-3xl md:text-5xl font-bold'>
            Let&rsquo;s Find Your Perfect Car<small className='text-[14px]'>...</small>
         </h1>
         <MediaQuery minWidth={'1200px'}>
            <Search />
         </MediaQuery>
      </section>
      <section className="flex flex-col gap-5 ml-4 md:ml-8 lg:ml-12">
         <div className="w-full flex items-center justify-between">
            <h3 className="text-blue-950 font-bold text-xl">
               Browse by Category
            </h3>
            <Link to={'/cartypes'} className="text-xs mr-5 md:mr-8 lg:mr-10 text-blue-950 font-bold flex items-center">
               <span className="pr-1">
                  View all
               </span>
               <MdArrowOutward />
            </Link>
         </div>
         <MediaQuery minWidth={'1200px'}>
            <CarTypes index={'12'} overflow={true} />
         </MediaQuery>
         <MediaQuery minWidth={'801px'} maxWidth={'1199px'}>
            <CarTypes index={'10'} overflow={true} />
         </MediaQuery>
         <MediaQuery maxWidth={'800px'}>
            <CarTypes index={'7'} overflow={true} />
         </MediaQuery>
      </section>
      <section className="flex flex-col gap-5 ml-4 md:ml-8 lg:ml-12">
         <div className="w-full flex items-center justify-between">
            <h3 className="text-blue-950 font-bold text-md lg:text-xl">
               Explore Our Premium Brands
            </h3>
            <Link  to={'/carbrands'} className="text-xs mr-5 md:mr-8 lg:mr-10 text-blue-950 font-bold flex items-center">
               <span className="pr-1">
                  View all
               </span>
               <MdArrowOutward />
            </Link>
         </div>
         <MediaQuery minWidth={'1200px'}>
            <CarBrands index={'12'} overflow={true} />
         </MediaQuery>
         <MediaQuery minWidth={'801px'} maxWidth={'1199px'}>
            <CarBrands index={'10'} overflow={true} />
         </MediaQuery>
         <MediaQuery maxWidth={'800px'}>
            <CarBrands index={'7'} overflow={true} />
         </MediaQuery>
      </section>
      <section 
         className="flex flex-col gap-4 py-10 pl-4 md:pl-8 lg:pl-12">
         <div className="w-full flex items-center justify-between">
            <h3 className="text-blue-950 font-bold text-xl">
               Featured Listings
            </h3>
            <Link to={'/featured'} className="text-xs mr-5 md:mr-8 lg:mr-10 text-blue-950 font-bold flex items-center">
               <span className="pr-1">
                  View all
               </span>
               <MdArrowOutward />
            </Link>
         </div>
         <MediaQuery minWidth={'801px'}>
            <Listin index={'12'} overflow={true}/> 
         </MediaQuery>
         <MediaQuery maxWidth={'801px'}>
            <Listin overflow={true}/> 
         </MediaQuery>
      </section>
      <section className="flex flex-col gap-8 py-10 pr-5 md:pl-8 pl-4 lg:pl-12 bg-gray-200 justify-center items-center">
         <h3 className="text-xl text-blue-950 font-bold">Why Choose Us</h3>
         <Box />
      </section>
      <DesktopFooter />
   </main>
  )
}

export default Home