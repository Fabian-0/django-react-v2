export const Logout = (handlerHistory) => {
  window.localStorage.clear()
  handlerHistory.replace('/')
  return true;
}

export function filterClasses({studentClasses, allClasses}) {
  const classesRef = studentClasses;
  let classesObj = {}
  let letJoin = []
  for (let i = 0; i < classesRef.length; i++) {
    const refName = classesRef[i].id;
    classesObj[refName] = refName;   
  }
  for (let i = 0; i < allClasses.length; i++) {
    if(classesObj[allClasses[i].id]) continue;
    letJoin.push(allClasses[i])
  }
  return letJoin
}