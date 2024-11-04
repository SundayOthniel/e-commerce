import { TbCarSuv } from "react-icons/tb";
import { useNavigate } from "react-router-dom";

function CarBrands({index=20, overflow=false}) {
   const navigate = useNavigate()
   let carBrands = [
      "Tesla", "Toyota", "Jeep", "Ford", "Chevrolet", "Ram", "Hyundai", "Kia", "BMW", "Mercedes-Benz", "Audi", "Subaru" , "Volkswagen", "Mazda"
   ];
    const slicedBrands = carBrands.slice(0, index)

    const handleBrand = (brand) => {
      localStorage.setItem('searchBrand', JSON.stringify(brand))
      navigate('/brands')
    }
  return (
    <div className={`flex ${ overflow ? 'w-[98%]  overflow-x-auto customScroll' : 'overflow-hidden ml-4 md:ml-8 lg:ml-14 flex-wrap gap-5'} gap-3`}>
      {
         slicedBrands.map((car) => (
            <div 
               className={`flex text-center flex-col cursor-pointer hover:bg-gray-200 hover:bg-clip-padding border rounded-md border-gray-400 items-center justify-center ${overflow ? 'min-w-[100px] h-[60px]' : 'min-w-[100px] h-[60px] md:min-w-[180px] md:h-[80px] lg:min-w-[250px] lg:h-[100px]'}`} 
               key={car}
               onClick={() => {handleBrand(car)}}
               >
                  <TbCarSuv />
                  <h4 
                     className=' text-[10px] text-blue-950 font-bold'>{car}
               </h4>
            </div>
         ))
      }
    </div>
  )
}

export default CarBrands
