import Search from '../../utils/search'
import { motion } from 'framer-motion'

function FindaCar() {
   const boxVariants = {
      initial: {
         scale: 0.5,
      },
      final: {
         scale: 1,
         transition: {
            type: 'tween',
         }
      }
   }
   return (
      <main className='w-[100%] h-[100vh] bg-img2 bg-cover'>
         <div
            
            className='w-[100%] h-[100%] backdrop-blur-lg justify-center items-center flex'>
            <motion.div
               variants={boxVariants} 
               initial='initial' 
               animate='final'>
               <Search />
            </motion.div>
         </div>
      </main>
   )
}

export default FindaCar
