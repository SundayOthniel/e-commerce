import { Link } from "react-router-dom"
import { MdArrowOutward } from "react-icons/md";
import { numberWithCommas } from "../carData/cars";

function ListinBox({car, index, show}) {
  return (
   <>
      <img src={car['carImage']} alt={`${car.carData} - ${car.sortedCarModels[car.carData]}`} loading="eager" rel="preload"  className={`rounded-t-lg bg-contain ${!show ? 'w-[150px] h-[100px] md:w-[180px]' : 'min-w-[250px] h-[100px] md:min-w-[300px] md:h-[150px]'}`} />
      <div className="flex flex-col gap-2 bg-white p-4 rounded-b-lg">
         <h5 className="text-blue-950 text-xs font-bold font-price">
            {car.condition} {car.carData} {car.sortedCarModels[car.carData]}
         </h5>
         <ul className="flex list-disc p-0 m-0">
            <li className="text-[9px] text-blue-950 font-extrabold mx-2">
               {car.fuelType}
            </li>
            <li className="text-[9px] text-blue-950 font-extrabold mx-2">
               {car.transmission}
            </li>
         </ul>
         <h5 className="font-extrabold text-md font-price">
            &#8358;{numberWithCommas(car.price)}
         </h5>
         <Link className="text-[10px] text-blue-600 font-bold flex items-center hover:text-blue-950">
            <span className="pr-1">
               View Details
            </span>
            <MdArrowOutward />
         </Link>
      </div>
   </>
  )
}

export default ListinBox
