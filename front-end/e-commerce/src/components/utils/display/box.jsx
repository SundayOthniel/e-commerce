import { FaHandshake, FaUserFriends, FaShieldAlt } from 
"react-icons/fa";
import { MdViewCarousel } from "react-icons/md";

function Box() {
  return (
   <div  className="flex gap-6 flex-wrap justify-center">
      <div className='w-[250px]  flex flex-col gap-3 bg-white rounded-xl shadow-md p-6'>
         <FaHandshake className="text-blue-500 mx-auto mb-4 h-8 w-8" />
         <h5 className='text-sm font-bold text-blue-950'>
            Guaranteed Hassle-Free Buying Experience
         </h5>
         <p className='text-[11px] tracking-wider'>
            Skip the haggling and paperwork headaches. Our streamlined process lets you focus on finding your perfect car.
         </p>
    </div>
    <div className='w-[250px]  flex flex-col gap-3 bg-white rounded-xl shadow-md p-6'>
         <MdViewCarousel className="text-blue-500 mx-auto mb-4 h-8 w-8" />
         <h5 className='text-sm font-bold text-blue-950'>
            Widest Selection, Competitive Prices
         </h5>
         <p className='text-[11px] tracking-wider'>
            Browse a vast inventory of vehicles to find the make,    model, and features you desire, all at fair and competitive prices.
         </p>
    </div>
    <div className='w-[250px]  flex flex-col gap-3 bg-white rounded-xl shadow-md p-6'>
         <FaUserFriends className="text-blue-500 mx-auto mb-4 h-8 w-8" />
         <h5 className='text-sm font-bold text-blue-950'>
            Expert Support, Every Step of the Way
         </h5>
         <p className='text-[11px] tracking-wider'>
            Our knowledgeable and friendly team is here to guide you through the entire buying process, from initial search to driving off the lot.
         </p>
    </div>
    <div className='w-[250px]  flex flex-col gap-3 bg-white rounded-xl shadow-md p-6'>
         <FaShieldAlt className="text-blue-500 mx-auto mb-4 h-8 w-8" />
         <h5 className='text-sm font-bold text-blue-950'>
            Commitment to Quality and Transparency
         </h5>
         <p className='text-[11px] tracking-wider'>
            We offer detailed vehicle inspections and upfront pricing so you can buy with confidence.
         </p>
    </div>
   </div>
    
  )
}

export default Box
