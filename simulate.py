from simulation import SIMULATION
from generate import Create_Brain

def eval(genes, penalty = False, onlyStraight = False):
	Create_Brain(genes)
	sim = SIMULATION(False)
	return sim.Run(1000, penalty, onlyStraight)

def demo():
	#Create_Brain(genes)
	sim = SIMULATION(True)
	sim.Demo(2500)

if __name__ == "__main__":
	#genes = [[0.13205872203558733, -0.3767514169081032, 0.29598204324561395, 0.005302962462529925, 0.183652863802086, 0.3234338437053137, 0.9928898536325061, 0.00802275562990018, -0.16372965080193358], [0.19551456951169655, -0.28050359155124216, -0.08039601314379008, 0.26080002803210167, 0.056612787974966716, -0.05823923600730496, 0.23315585154179996, -0.26939588132614056, 0.25310383320389207], [0.3182432869428846, 0.11218418033061528, -0.060096598472667906, 0.22400315296050255, -0.27967918544824133, -0.4015115816645901, 0.09764522558974642, -0.1739895005741522, -0.2815097321676079], [-0.4968949563971272, 0.14442391549309597, 0.18402992045665467, -0.3960840348282617, -0.11214751040938564, -0.6081532652187529, -0.0439637440477586, 0.07446068034606879, -0.17459301734502897], [0.36856552343177296, 0.7525505361044249, 0.3830453027833539, 0.3081532140726314, 0.042741651212145126, 0.4961545460414284, 0.08650964860043886, 0.20609385236410982, 0.3448960343124], [-0.464292895772657, -0.4183691901594624, 0.11669632384295281, -0.11045594068765685, 0.49808698513202687, 0.051293058198199404, -0.2280471450548085, 0.43180243172436183, 0.047710847794765976], [0.14306929254230583, -0.43892462705688307, -0.5245266933853436, 0.11882993826994004, 0.4314721042530617, -0.43115971599900305, -0.45606715841876044, -0.1437523342482745, 0.13789396817210553], [0.3465225274197099, -0.24060042174679663, 0.3317992709527253, 0.2832152838261235, 0.2739355640488188, 0.09527661422063605, 0.1847412222882827, -0.4012123134106502, 0.2743745518474089]]
	#genes = [[0.06969788561723259, 0.059728601486699326, 0.08782256718297668, 0.03721896556155072, 0.07125275373334826, 0.05515319406806658, 0.07128010616217151, 0.09613363737723389, 0.06108662892295006], [0.08392505573928882, 0.011850693370292643, 0.01774232182879092, 0.05761938615010204, 0.07103426062912174, 0.009311691565338487, 0.07935049571635434, 0.012807290498420443, 0.08212871925558551], [0.0949461981929034, 0.06621331750367888, 0.04525552963756822, 0.05275546332598435, 0.08654495062025842, 0.3992862774064161, 0.08142037266646401, 0.055173247661222516, 0.021216326387140973], [0.30713062124918666, 0.006623174142686839, 0.08590876541790371, 0.02082537493587926, 0.021311785532140626, 0.01148355629208032, 0.4857847132948149, 0.09269919898755213, 0.024787262885364203], [0.04825538735128456, 0.04143092183698419, 1.746407832738939e-05, 0.045868269851085296, 0.002429999547514039, 0.0311089769655987, 0.04605615582228233, 0.08895560373738745, 0.01689799704973589], [0.05540349917847172, 0.003155798653513897, 0.0037184806596942898, 0.0759004796237144, 0.08857715775734469, 0.11646452383274153, 0.06794381746814811, 0.0767813632362524, 0.0423191832568239], [0.09749798993861102, 0.00663541354633348, 0.06074300306981575, 0.028783452872849613, 0.07932797229468569, 0.04748572032223604, 0.09786711900484696, 0.008369582473531246, 0.07270986368606351], [0.04525652553934316, 0.051017901845324856, 0.05307255519463663, 0.05669348571010731, 0.07412762851993657, 0.008497977658839195, 0.07789206638610836, 0.0060124038174460435, 0.004248336429022737]]
	#genes = [[0.06589096088401089, 0.058174118669157414, 0.05373744834376311, 0.13976829979831962, 0.06808691572366148, 0.09469283490451927, 0.05805446339792732, 0.006494004335341097, 0.06474074030037663], [0.24366111049173855, 0.07678626432986088, 0.6019588950159074, 0.09725823784133711, 0.073918748444841, 0.05540797833330006, 0.05546091898057472, 0.06437376730477098, 0.02672517469669209], [0.0439495967169745, 0.040638341192408424, 0.07857505513217651, 0.05545069793601829, 0.03089294997856725, 0.09730024876305075, 0.03109637656840526, 0.0329712814590196, 0.07369906533930551], [0.09836413534773877, 0.021598814399208556, 0.09401876322788384, 0.031048415653353534, 0.035715787598941465, 0.042274617321482647, 0.05485773010082542, 0.0438241150678218, 0.03264918975544493], [0.049540357145788194, 0.06543599958604933, 0.04447993688506805, 0.08040367083325202, 0.5349351593840108, 0.08048421822388854, 0.08321146665365915, 0.04815882704630997, 0.09319745931325503], [0.017147894626030315, 0.002077522485770622, 0.07778347585312241, 0.05322494094401655, 0.0731806428415905, 0.06300078726600893, 0.0715981361302451, 0.016736700471009856, 0.06250572172215366], [0.027880026012815494, 0.09273331924621875, 0.08397210890066939, 0.038039622066553216, 0.03534188954505747, 0.03747018576000979, 0.01585954921863525, 0.051786335392801905, 0.005804637032811477], [0.07652706842628296, 0.011079997867730885, 0.07545604993610446, 0.08177696040148848, 0.05795933984182995, 0.06366262089348272, 0.07974898388259369, 0.03576652484358509, 0.050993536522905614]]
	#genes = [[0.06326522466643066, 0.11382791799477587, 0.010435766133459668, 0.010120097050018418, 0.025806448231696644, 0.7788211363213127, 0.7317357894798183, 0.22076814855425053, 0.5092572792408817], [0.2432639168545414, 0.059668046565810595, 0.08630579178708755, 0.09041375004330197, 0.00326388430444251, 0.9487389407190036, 0.11121486458433727, 0.15395154887279994, 0.5304681701434741], [0.435158318166991, 0.042529224179372604, 0.06550532685667454, 0.06444712574770814, 0.558055104547763, 0.01565958980538713, 0.06477950317466011, 0.04675236329367398, 0.5324847645453905], [0.6127960248374124, 0.0871698754112552, 0.08822431946565507, 0.9011795699230127, 0.5927558038075749, 0.7350382466892833, 0.014438425639000297, 0.9692961633137168, 0.7867158534635533], [0.8098597965958862, 0.06853610050011624, 0.03610298947665611, 0.013870875350261703, 0.0547819025707922, 0.9458979077990638, 0.035762042617443354, 0.3117041877017568, 0.5424580468273812], [0.09382997407168547, 0.9219196782658845, 0.16549158346834036, 0.07067525341640674, 0.07952199251991621, 0.8413266124607373, 0.9089069028774402, 0.09152643983025295, 0.04675931570940972], [0.7498299931097497, 0.0068717771787492055, 0.628151086328195, 0.010347809769797323, 0.6166477116250659, 0.003662731543087805, 0.32483150993385457, 0.08782784089178107, 0.3220578489200824], [0.8519529355155896, 0.9642560492314336, 0.04321151432730801, 0.9762527094095057, 0.9761506801524297, 0.05485330598291582, 0.057929396131852585, 0.5732609643987545, 0.9755681852494663]]
	#genes = [[0, 0, 0, 0, 0, 0, 0, 0], [0.35098947346961773, 0, 0.24644477451675728, 0.3007514072763925, 0.2562530989248867, 0, 0.5865888996330286, 0], [0.6939855435744339, 0, 0.9104437807473579, 0.29910080831719843, 0, 0.34977336705692696, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0.18078344734629437], [0, 0.531968684076027, 0, 0, 0, 0, 0, 0.12504733722088746], [0, 0, 0, 0.7460448240606624, 0, 0, 0.54152601293881, 0], [0.18093820451158404, 0.2174746503412156, 0.32777339427738983, 0.28957838450832496, 0, 0.6683428258862323, 0, 0], [0, 0, 0, 0.28684402943872045, 0, 0, 0, 0.1074603144257108]]
	#genes = [[0.20845156348045857, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0.2755770652329016, 0.14662148595868918, 0.5231858965038875, 0, 0, 0.053003787385354606, 0, 0.8480036494925484], [0, 0.8662386389890457, 0, 0, 0, 0, 0, 0.8013096349007186], [0.3191281068587728, 0.05170989161118733, 0, 0, 0, 0, 0, 0], [0, 0.9041939452919305, 0, 0.17278995647971873, 0, 0, 0, 0.5519055625478294], [0, 0.1115117136370094, 0, 0, 0, 0, 0, 0.48134164282360425], [0, 0, 0, 0, 0, 0, 0, 0]]
	demo()