import { Link } from 'react-router-dom'

function ErrorPage() {
  return (
    <div className='flex items-center justify-center bg-blue-800 w-full h-screen lg:h-auto md:h-auto'>
      <Link to={'/'}> <img src='/components/utils/404-error.jpg' alt="PAGE NOT FOUND. CLICK TO RETURN TO MAIN PAGE" /> </Link>
    </div>
  )
}

export default ErrorPage