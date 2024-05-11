const Notification = ({personality}) => {
  return (
    <div className="fixed flex flex-col rounded-md shadow-2xl justify-around items-center top-1/2 left-1/2 translate-x-center translate-y-center bg-wheat md:w-2/5 w-4/5 md:h-2/5 h-2/5">
        <h2 className="lg:text-3xl text-2xl font-semibold mt-9">Giới tính của bạn là:</h2>
        <p className="lg:text-2xl text-xl">{personality}</p>
        <p className="text-center">Nhấn F5 để thử lại</p>
    </div>
  )
}
export default Notification