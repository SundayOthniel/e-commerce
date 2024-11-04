import { motion } from 'framer-motion';

const Modal = ({ children, isOpen, onClose }) => {
  if (!isOpen) return null; // Don't render if not open

  return (
    <motion.div
      initial={{ scale: 0.8, opacity: 0 }}
      animate={{ oscale: 1, pacity: 1 }}
      exit={{ scale: 0.8, opacity: 0 }}
      transition={{ duration: 0.3 }}
      className="modal"
      onClick={onClose}
    >
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        {children}
      </div>
    </motion.div>
  );
};
export default Modal