const Mock = require('mockjs')
Mock.mock('/api/switch', 'get', function (options) {
  return {
    records: [
      {
        dpid: 1,
        id: 1,
        flow: [
          {
            text: 1.1
          },
          {
            text: 1.2
          }
        ]
      },
      {
        dpid: 2,
        id: 2,
        flow: [
          {
            text: 2.1
          },
          {
            text: 2.2
          }
        ]
      },
      {
        dpid: 3,
        id: 3,
        flow: [
          {
            text: 3.1
          },
          {
            text: 3.2
          }
        ]
      },
      {
        dpid: 4,
        id: 4,
        flow: [
          {
            text: 4.1
          },
          {
            text: 4.2
          }
        ]
      }
    ]
  }
})
Mock.mock('/api/addlink', 'post', (options) => {
  console.log(options)
  return {

  }
})
Mock.mock('/api/delhost', 'post', (options) => {
  console.log(options)
  return {

  }
})
Mock.mock('/api/dellink', 'post', (options) => {
  console.log(options)
  return {

  }
})
Mock.mock('/api/addflow', 'post', (options) => {
  console.log(options)
  return {

  }
})
Mock.mock('/api/addswitch', 'post', (options) => {
  console.log(options)
  return {

  }
})
Mock.mock('/api/delflow', 'delete', function(options) {
  console.log(options)
  return {

  }
})
Mock.mock('/api/addlink', 'post', (options) => {
  console.log(options)
  return {

  }
})
Mock.mock('/api/delswitch', 'post', (options) => {
  console.log(options)
  return {

  }
})
Mock.mock('/api/seepicture', 'post', (options) => {
  console.log(options)
  return {

  }
})
Mock.mock('/api/subflow', 'delete', (options) => {
  console.log(options)
  return {

  }
})
Mock.mock('/api/addhost', 'post', (options) => {
  console.log(options)
  return {

  }
})
