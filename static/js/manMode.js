function turn(target) {
    url = '/showTable?obj='+target+'&cond=2>1'
    console.log(url)
    $(location).prop('href',url)


}

// $('#L1').click(turn)